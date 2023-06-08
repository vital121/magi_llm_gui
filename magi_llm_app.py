import configparser
import csv
import glob
import platform
import sys
from datetime import datetime
from functools import partial
from pathlib import Path

import yaml
from PySide6 import QtWidgets
from PySide6.QtCore import QSize, QThread, Signal, Slot
from PySide6.QtGui import QIcon, QTextCursor
from PySide6.QtWidgets import QApplication, QFileDialog

from settings_window import Ui_Settings_Dialog
from ui_magi_llm_ui import Ui_magi_llm_window

# Constants for the directories and file names
APP_ICON = Path("appicon.png")
CHAT_PRESETS_DIR = Path("presets/instruct")
CHARACTER_PRESETS_DIR = Path("presets/character")
PROMPTS_FILE = Path("presets/prompts.csv")
SETTINGS_FILE = Path("settings.ini")


class TextgenThread(QThread):
    """A class to run text generation in a separate thread."""

    resultReady = Signal(str)
    final_resultReady = Signal(str)

    def __init__(
        self,
        exllama_params: dict,
        message: str,
        stream_enabled: bool,
        run_backend: str,
        cpp_params: dict,
    ):
        """Initialize the thread with the given parameters.

        Args:
            exllama_params (dict): The parameters for the exllama model.
            message (str): The input message to generate a response.
            stream_enabled (bool): Whether to enable streaming mode or not.
            run_backend (str): The backend to use for text generation ("exllama" or "llama.cpp").
            cpp_params (dict): The parameters for the llama.cpp model.
        """
        super().__init__()
        self.exllama_params = exllama_params
        self.message = message
        self.stream_enabled = stream_enabled
        self.run_backend = run_backend
        self.cpp_params = cpp_params

        self.stop_flag = False

    def run(self):
        """Run the text generation process and emit signals with the results."""

        if self.run_backend == "exllama":

            if self.stream_enabled:
                replies = []

                for response in exllama_model.generate_with_streaming(
                    self.message, self.exllama_params
                ):
                    replies.append(response)

                    if len(replies) > 1:
                        # Remove the previous response from the current one
                        stripped_response = replies[1].replace(replies[0], "")
                        replies.pop(0)
                        self.resultReady.emit(stripped_response)
                    else:
                        self.resultReady.emit(response)

                    if self.stop_flag:
                        break

                response = str(response)
                self.final_resultReady.emit(response)

            else:

                response = exllama_model.generate(
                    exllama_model, self.message, self.exllama_params
                )
                self.final_resultReady.emit(response)

        if self.run_backend == "llama.cpp":
            final_response = ""
            for response in cpp_model.generate(
                self.message,
                self.cpp_params["token_count"],
                self.cpp_params["temperature"],
                self.cpp_params["top_p"],
                self.cpp_params["top_k"],
                self.cpp_params["repetition_penalty"],
                self.cpp_params["mirostat_mode"],
            ):

                if self.stream_enabled:
                    self.resultReady.emit(response)
                final_response += response
                final_text = f"{self.message}{final_response}"

                if self.stop_flag:
                    break
            self.final_resultReady.emit(final_text)

    def stop(self):
        """Set the stop flag to True."""
        self.stop_flag = True


# Define a class for the SettingsWindow
class SettingsWindow(QtWidgets.QWidget, Ui_Settings_Dialog):
    # Initialize the window
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Set the window icon
        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        # Initialize flags for whether the models are loaded or not
        self.cpp_model_loaded = False
        self.exllama_model_loaded = False

        # Connect the settings sliders to the spin boxes
        self.temperatureSlider.valueChanged.connect(
            lambda: self.temperatureSpin.setValue(
                self.temperatureSlider.value() / 100)
        )
        self.top_pSlider.valueChanged.connect(
            lambda: self.top_pSpin.setValue(self.top_pSlider.value() / 100)
        )
        self.repetition_penaltySlider.valueChanged.connect(
            lambda: self.repetition_penaltySpin.setValue(
                self.repetition_penaltySlider.value() / 100
            )
        )

        # Connect the spin boxes to the settings sliders
        self.temperatureSpin.valueChanged.connect(
            lambda: self.temperatureSlider.setValue(
                self.temperatureSpin.value() * 100)
        )
        self.top_pSpin.valueChanged.connect(
            lambda: self.top_pSlider.setValue(self.top_pSpin.value() * 100)
        )
        self.repetition_penaltySpin.valueChanged.connect(
            lambda: self.repetition_penaltySlider.setValue(
                self.repetition_penaltySpin.value() * 100
            )
        )

        # Define a function to load parameters presets
        def load_params():
            # Get the list of yaml files in the presets folder
            param_preset_load = glob.glob("presets/model_params/*.yaml")
            # Loop over the files and add their names to the combo box
            for param_preset in param_preset_load:
                param_preset_stem = Path(param_preset).stem
                self.paramPresets_comboBox.addItem(param_preset_stem)

            # Set the default preset to _MAGI_DEFAULT
            self.paramPresets_comboBox.setCurrentText("_MAGI_DEFAULT")

        # Call the function to load parameters presets
        load_params()

        def set_params():
            # Load and set parameters
            config = configparser.ConfigParser()
            config.read('settings.ini')

            ### Define params ###
            # Params-Shared
            temperature = config["Params-Shared"]["temperature"]
            top_k = config["Params-Shared"]["top_k"]
            top_p = config["Params-Shared"]["top_p"]
            max_new_tokens = config["Params-Shared"]["max_new_tokens"]
            repetition_penalty = config["Params-Shared"]["repetition_penalty"]
            seed = config["Params-Shared"]["seed"]

            # Params-Exllama
            min_p = config["Params-Exllama"]["min_p"]
            token_repetition_penalty_decay = config["Params-Exllama"]["token_repetition_penalty_decay"]
            num_beams = config["Params-Exllama"]["num_beams"]
            beam_length = config["Params-Exllama"]["beam_length"]

            # Params-LlamaCPP
            threads = config["Params-LlamaCPP"]["threads"]
            context_size = config["Params-LlamaCPP"]["context_size"]
            repeat_last_n = config["Params-LlamaCPP"]["repeat_last_n"]
            batch_size = config["Params-LlamaCPP"]["batch_size"]
            mirostat_mode = config["Params-LlamaCPP"]["mirostat_mode"]
            n_gpu_layers = config["Params-LlamaCPP"]["n_gpu_layers"]
            lora_path = config["Params-LlamaCPP"]["lora_path"]

            use_mmap = config["Params-LlamaCPP"]["use_mmap"]
            use_mlock = config["Params-LlamaCPP"]["use_mlock"]
            use_gpu_accel = config["Params-LlamaCPP"]["use_gpu_accel"]

            ### Set params ###
            # Params-Shared
            self.temperatureSpin.setValue(float(temperature))
            self.temperatureSlider.setValue(int(float(temperature)*100))

            self.top_kSpin.setValue(int(top_k))
            self.top_kSlider.setValue(int(top_k))

            self.top_pSpin.setValue(float(top_p))
            self.top_pSlider.setValue(int(float(top_p)*100))

            self.max_new_tokensSpin.setValue(int(max_new_tokens))
            self.max_new_tokensSlider.setValue(int(max_new_tokens))

            self.repetition_penaltySpin.setValue(float(repetition_penalty))
            self.repetition_penaltySlider.setValue(
                int(float(repetition_penalty)*100))

            self.seedSpin.setValue(int(seed))

            # Params-Exllama
            self.minPSpin.setValue(float(min_p))
            self.minPSlider.setValue(int(min_p))

            self.token_repetition_penalty_decaySpin.setValue(
                int(token_repetition_penalty_decay))
            self.token_repetition_penalty_decaySlider.setValue(
                int(token_repetition_penalty_decay))

            self.numbeamsSpin.setValue(int(num_beams))
            self.numbeamsSlider.setValue(int(num_beams))

            self.beamLengthSpin.setValue(int(beam_length))
            self.beamLengthSlider.setValue(int(beam_length))

            # Params-LlamaCPP
            self.cppThreads.setValue(int(threads))

            self.CPP_ctxsize_Spin.setValue(int(context_size))
            self.CPP_ctxsize_Slider.setValue(int(context_size))

            self.CPP_repeat_last_nSpin.setValue(int(repeat_last_n))
            self.CPP_repeat_last_nSlider.setValue(int(repeat_last_n))

            self.cppBatchSizeSpin.setValue(int(batch_size))
            self.cppBatchSizeSlider.setValue(int(batch_size))

            self.gpuLayersSpin.setValue(int(n_gpu_layers))
            self.gpuLayersSlider.setValue(int(n_gpu_layers))

            self.cppLoraLineEdit.setText(str(lora_path))
            self.cppMirastatMode.setValue(int(mirostat_mode))

            self.cppMmapCheck.setChecked(eval(use_mmap))
            self.cppMlockCheck.setChecked((eval(use_mlock)))
            self.gpuAccelCheck.setChecked(eval(use_gpu_accel))

        set_params()

        # Define a function to apply parameters presets
        def apply_params_preset():

            # Get the current preset from the combo box
            current_preset = self.paramPresets_comboBox.currentText()
            # Construct the file name for the preset
            preset_file = f"presets/model_params/{current_preset}.yaml"

            # Open the file and load the parameters as a dictionary
            with open(preset_file, "r") as file:
                param_preset_name = yaml.safe_load(file)

            # Set the values of the spin boxes and sliders according to the parameters
            self.top_pSpin.setValue(float(param_preset_name["top_p"]))
            self.top_pSlider.setValue(int(param_preset_name["top_p"] * 100))
            self.top_kSpin.setValue(int(param_preset_name["top_k"]))
            self.top_kSlider.setValue(int(param_preset_name["top_k"]))
            self.temperatureSpin.setValue(
                float(param_preset_name["temperature"]))
            self.temperatureSlider.setValue(
                int(param_preset_name["temperature"] * 100))
            self.repetition_penaltySpin.setValue(
                float(param_preset_name["repetition_penalty"]))
            self.repetition_penaltySlider.setValue(
                int(param_preset_name["repetition_penalty"] * 100)
            )

            # Print a message indicating which preset was applied
            print("--- Applied parameter preset:", preset_file)

        # Connect the function to the combo box signal
        self.paramPresets_comboBox.currentTextChanged.connect(
            lambda: apply_params_preset())


class ChatWindow(QtWidgets.QMainWindow, Ui_magi_llm_window):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.settings_win = SettingsWindow()

        icon = QIcon()
        icon.addFile(str(APP_ICON), QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)

        self.model_load = False

        # Load chat presets
        self.load_presets(CHAT_PRESETS_DIR, self.instructPresetComboBox)

        # Load character presets
        self.load_presets(CHARACTER_PRESETS_DIR, self.characterPresetComboBox)

        # Load awesome prompts
        self.load_prompts(PROMPTS_FILE)

        self.set_preset_params('instruct')

        # Load settings
        self.load_settings(SETTINGS_FILE)

    def load_presets(self, directory, combo_box):
        # Load presets from a given directory and populate a combo box.
        presets = glob.glob(f"{directory}/*.yaml")
        for preset in presets:
            preset_stem = Path(preset).stem
            combo_box.addItem(preset_stem)

    def load_prompts(self, filename):
        # Load prompts from a CSV file and populate a combo box.
        with open(filename, "r",  encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                self.awesomePresetComboBox.addItem(row[0])
            self.awesomePresetComboBox.removeItem(0)

    def load_settings(self, filename: str):

        # Load settings from an INI file and set the corresponding widgets.

        config = configparser.ConfigParser()
        config.read(filename)
        self.cppModelPath.setText(config["Settings"]["cpp_model_path"])
        self.exllamaModelPath.setText(config["Settings"]["exllama_model_path"])

        # Button clicks
        self.defaultGenerateButton.clicked.connect(
            partial(self.textgen_switcher, 'default_mode'))
        self.notebookGenerateButton.clicked.connect(
            partial(self.textgen_switcher, 'notebook_mode'))
        self.chatGenerateButton.clicked.connect(
            partial(self.textgen_switcher, 'chat_mode'))

        self.defaultContinueButton.clicked.connect(
            partial(self.continue_textgen, 'default_modeContinue'))
        self.notebookContinueButton.clicked.connect(
            partial(self.continue_textgen, 'notebook_modeContinue'))
        self.chatContinueButton.clicked.connect(
            partial(self.continue_textgen, 'chat_modeContinue'))

        self.defaultStopButton.clicked.connect(self.stop_textgen)
        self.notebookStopButton.clicked.connect(self.stop_textgen)
        self.chatStopButton.clicked.connect(self.stop_textgen)

        self.paramWinShowButton.clicked.connect(self.settings_win.show)

        self.settingsPathSaveButton.clicked.connect(self.save_settings)

        self.chatClearButton.clicked.connect(
            partial(self.set_preset_params, 'instruct'))

        self.cppModelSelect.clicked.connect(self.cpp_model_select)
        self.exllamaModelSelect.clicked.connect(self.exllama_model_select)

        self.instructPresetComboBox.currentTextChanged.connect(
            partial(self.set_preset_params, 'instruct'))
        self.characterPresetComboBox.currentTextChanged.connect(
            partial(self.set_preset_params, 'character'))
        self.instructRadioButton.clicked.connect(
            partial(self.set_preset_params, 'instruct'))
        self.charactersRadioButton.clicked.connect(
            partial(self.set_preset_params, 'character'))

        self.awesomePresetComboBox.currentTextChanged.connect(
            self.awesome_prompts)

        # Quit from menu
        self.actionSettings.triggered.connect(self.settings_win.show)
        self.actionExit.triggered.connect(app.exit)

        # Status bar
        self.statusbar.showMessage("Status: Ready")

    # Define a helper function to get the file path from a dialog
    def get_file_path(self, title, filter):
        file_path = (QFileDialog.getOpenFileName(
            self, title, '', filter)[0])
        return file_path

    # Define a helper function to get the directory path from a dialog
    def get_directory_path(self, title):
        directory_path = str(QFileDialog.getExistingDirectory(
            self, title))
        return directory_path

    # Browse for the GGML model
    def cpp_model_select(self):
        file_x = self.get_file_path('Open file', "GGML models (*bin)")

        if file_x:
            self.cppModelPath.setText(file_x)

    def exllama_model_select(self):
        file_x = self.get_directory_path("Select Directory")

        if file_x:
            self.exllamaModelPath.setText(file_x)

    def save_settings(self):

        config = configparser.ConfigParser()
        config.read("settings.ini")
        config.set("Settings", "cpp_model_path", self.cppModelPath.text())
        config.set("Settings", "exllama_model_path",
                   self.exllamaModelPath.text())

        with open("settings.ini", "w") as f:
            # Write the ConfigParser object to the file
            config.write(f)
        f.close()

        print('Settings saved')

    def history_readonly_logic(self, readonly_mode: bool):
        """Set the history widget and the buttons to readonly mode or not.

        Args:
            readonly_mode (bool): Whether to enable readonly mode or not.
        """

        # A dictionary to map the textgen modes to the corresponding widgets
        mode_widgets = {
            "notebook_mode": self.notebook_modeTextHistory,
            "chat_mode": self.chat_modeTextHistory,
        }

        # Set the history widget to readonly mode based on the textgen mode
        history_widget = mode_widgets.get(textgen_mode)
        if history_widget:
            history_widget.setReadOnly(readonly_mode)

        # Invert readonly_mode for buttons
        button_mode = not readonly_mode

        # A list of buttons to enable or disable based on the button mode
        buttons = [
            self.instructPresetComboBox,
            self.characterPresetComboBox,
            self.streamEnabledCheck,
            self.defaultContinueButton,
            self.notebookContinueButton,
            self.chatContinueButton,
            self.defaultGenerateButton,
            self.notebookGenerateButton,
            self.chatGenerateButton,
            self.defaultClearButton,
            self.notebookClearButton,
            self.chatClearButton,
        ]

        # Iterate over the buttons and set their enabled status
        for button in buttons:
            button.setEnabled(button_mode)

    # Stop button logic

    def stop_textgen(self):
        self.textgenThread.stop()

        # Disable all stop buttons
        for button in [self.defaultStopButton, self.notebookStopButton, self.chatStopButton]:
            button.setEnabled(False)

    # Continue button logic
    def continue_textgen(self, text_tab):

        if not self.exllamaCheck.isEnabled():
            if self.exllamaCheck.isChecked():
                run_backend = 'exllama'
            else:
                run_backend = 'llama.cpp'

            # Get the history text from the corresponding tab
            history_text = getattr(self, text_tab.replace(
                'Continue', 'TextHistory')).toPlainText()

            # Launch the backend with the history text and the run backend
            self.launch_backend(history_text, run_backend)

            # Set the history readonly logic to True
            self.history_readonly_logic(True)

    # Define a helper function to insert text and scroll to the end of a text widget
    def insert_text_and_scroll(self, text_widget, text):
        cursor = text_widget.textCursor()
        cursor.movePosition(QTextCursor.End)  # Move it to the end
        cursor.insertText(text)
        text_widget.verticalScrollBar().setValue(
            text_widget.verticalScrollBar().maximum())

    @Slot(str)
    def handleResult(self, reply):

        # Get the text widget from the textgen mode
        text_widget = getattr(self, textgen_mode + 'TextHistory')

        # Insert the reply and scroll to the end
        self.insert_text_and_scroll(text_widget, reply)

    # Handle the final response from textgen
    @Slot(str)
    def final_handleResult(self, final_text):

        if not self.streamEnabledCheck.isChecked():
            # Get the text widget from the textgen mode
            text_widget = getattr(self, textgen_mode + 'TextHistory')

            # Set the plain text to the final text
            text_widget.setPlainText(final_text)

        # Write chat log
        if textgen_mode == 'chat_mode' and self.logChatCheck.isChecked():
            current_date = self.get_chat_date()

            with open(f"logs/chat_{current_date}.txt", "a", encoding='utf-8') as f:
                f.write('\n'+final_text)
            print('Wrote chat log')

        self.statusbar.showMessage(f"Status: Generation complete")
        self.history_readonly_logic(False)

        # Stop the textgen thread
        self.stop_textgen()

    # Get the llama.cpp parameters
    def get_llama_cpp_params(self):

        cpp_params = {
            'token_count': int(self.settings_win.max_new_tokensSpin.value()),
            'temperature': float(self.settings_win.temperatureSpin.value()),
            'top_p': float(self.settings_win.top_pSpin.value()),
            'top_k': int(self.settings_win.top_kSpin.value()),
            'repetition_penalty': float(self.settings_win.repetition_penaltySpin.value()),
            'mirostat_mode': int(self.settings_win.cppMirastatMode.value())
        }

        return cpp_params

    # Get the Exllama parameters
    def get_exllama_params(self):

        exllama_params = {
            'max_new_tokens': self.settings_win.max_new_tokensSpin.value(),
            'temperature': self.settings_win.temperatureSpin.value(),
            'top_p': self.settings_win.top_pSpin.value(),
            'repetition_penalty': self.settings_win.repetition_penaltySpin.value(),
            'top_k': self.settings_win.top_kSpin.value(),
            'num_beams': self.settings_win.numbeamsSpin.value(),
            'beam_length': self.settings_win.beamLengthSpin.value(),
            'min_p': self.settings_win.minPSpin.value(),
            'token_repetition_penalty_sustain': self.settings_win.token_repetition_penalty_decaySpin.value(),
        }

        return exllama_params

    # Get data for chat log save
    def get_chat_date(self):
        today = datetime.today()
        day = today.day
        month = today.month
        year = today.year
        return (f'{day}-{month}-{year}')

    # Set chat prefixes
    def get_chat_presets(self, chat_mode):

        # Get the preset name from the corresponding combo box
        preset_name = getattr(self, chat_mode + 'PresetComboBox').currentText()

        # Get the preset file path from the chat mode and the preset name
        preset_file = f"presets/{chat_mode}/{preset_name}.yaml"

        # Load the preset file as a dictionary
        with open(preset_file, 'r') as file:
            chat_preset = yaml.safe_load(file)

        return chat_preset

    # Define a helper function to get the model path from a line edit widget
    def get_model_path(self, line_edit):
        model_path = line_edit.text().strip()
        return model_path

    # Define a helper function to get the cpp model parameters from the settings window
    def get_cpp_model_params(self):

        cpp_model_params = {
            'model_path': self.get_model_path(self.cppModelPath),
            'seed': self.settings_win.seedSpin.value(),
            'n_threads': self.settings_win.cppThreads.value(),
            'n_batch': self.settings_win.cppBatchSizeSpin.value(),
            'n_ctx': self.settings_win.CPP_ctxsize_Spin.value(),
            'use_mmap': self.settings_win.cppMmapCheck.isChecked(),
            'use_mlock': self.settings_win.cppMlockCheck.isChecked(),
        }

        # Add optional params
        if self.settings_win.gpuAccelCheck.isChecked():
            cpp_model_params["n_gpu_layers"] = self.settings_win.gpuLayersSpin.value(
            )
        if self.settings_win.cppLoraLineEdit.text():
            cpp_model_params["lora_path"] = self.get_model_path(
                self.settings_win.cppLoraLineEdit)

        return cpp_model_params

    # Load models
    def load_model(self, model_name):

        # Print a message indicating which model is being loaded
        print(f'--- Loading {model_name} model...')

        # Declare global variables for the models and the tokenizer
        global exllama_model, cpp_model, tokenizer
        # Load the model and the tokenizer based on the model name
        if model_name == 'Exllama':
            from api_fetch import ExllamaModel
            exllama_model, tokenizer = ExllamaModel.from_pretrained(
                self.get_model_path(self.exllamaModelPath))
            print(f'--- Exllama model load parameters:',
                  self.get_model_path(self.exllamaModelPath))

        elif model_name == 'llama.cpp':
            from llamacpp_model_generate import LlamaCppModel

            cpp_model, tokenizer = LlamaCppModel.from_pretrained(
                self.get_cpp_model_params())
            print('--- llama.cpp model load parameters:',
                  self.get_cpp_model_params())

    def set_textgen_things(self):
        # Set the history to read-only mode
        self.history_readonly_logic(True)

        # Enable the stop buttons for each mode
        self.defaultStopButton.setEnabled(True)
        self.notebookStopButton.setEnabled(True)
        self.chatStopButton.setEnabled(True)

    # Main launcher logic
    def textgen_switcher(self, pre_textgen_mode):
        # Check if the model has been loaded
        if not self.model_load:
            # Load the model based on the user's choice of cpp or exllama
            if self.cppCheck.isChecked():
                self.load_model('llama.cpp')
            elif self.exllamaCheck.isChecked():
                self.load_model('Exllama')

            # Set the model_load flag to True
            self.model_load = True
            # self.chatGenerateButton.setText("Generate")

            # Disable the cpp and exllama checkboxes
            self.cppCheck.setEnabled(False)
            self.exllamaCheck.setEnabled(False)

        # Declare a global variable for the textgen mode
        global textgen_mode
        # Set the textgen mode to the pre-textgen mode argument
        textgen_mode = pre_textgen_mode

        # If the pre-textgen mode is default mode
        if pre_textgen_mode == 'default_mode':
            input_message = self.defaultTextInput.toPlainText()
            # If the input message is not empty
            if input_message:
                # Set the default mode text history widget to show the input message
                self.default_modeTextHistory.setPlainText(input_message)
                # Choose the backend based on the cpp checkbox status
                backend = 'llama.cpp' if self.cppCheck.isChecked() else 'exllama'
                # Launch the backend with the input message and the backend name
                self.launch_backend(input_message, backend)

        # If the pre-textgen mode is notebook mode
        if pre_textgen_mode == 'notebook_mode':
            input_message = self.notebook_modeTextHistory.toPlainText()
            # If the input message is not empty
            if input_message:
                # Choose the backend based on the cpp checkbox status
                backend = 'llama.cpp' if self.cppCheck.isChecked() else 'exllama'
                # Launch the backend with the input message and the backend name
                self.launch_backend(input_message, backend)

        # If the pre-textgen mode is chat mode
        if pre_textgen_mode == 'chat_mode':
            # Get the input message from the chat mode text input widget
            input_message = self.chat_modeTextInput.toPlainText()

            # If the input message is not empty
            if input_message:
                # Generate a final prompt by calling the prompt_generation method with the pre-textgen mode argument
                final_prompt = self.prompt_generation(pre_textgen_mode)
                # Set the chat mode text history widget to show the final prompt
                self.chat_modeTextHistory.setPlainText(final_prompt)

                # Choose the backend based on the cpp checkbox status
                backend = 'llama.cpp' if self.cppCheck.isChecked() else 'exllama'
                # Launch the backend with the final prompt and the backend name
                self.launch_backend(final_prompt, backend)

                # Clear the chat mode text input widget
                self.chat_modeTextInput.clear()

    # Launch QThread to textgen
    def launch_backend(self, message, run_backend):
        # Get the exllama and cpp parameters from their respective methods
        exllama_params = self.get_exllama_params()
        cpp_params = self.get_llama_cpp_params()

        # Show a status message indicating that the generation is in progress
        self.statusbar.showMessage(f"Status: Generating...")

        # Create a textgenThread object with the exllama and cpp parameters, the message, the stream enabled status, and the backend name
        self.textgenThread = TextgenThread(
            exllama_params, message,
            self.streamEnabledCheck.isChecked(), run_backend, cpp_params)

        # Connect signals and slots
        self.textgenThread.resultReady.connect(self.handleResult)
        self.textgenThread.final_resultReady.connect(self.final_handleResult)
        self.textgenThread.finished.connect(self.textgenThread.deleteLater)

        # Start the thread
        self.textgenThread.start()
        # Set the textgen things
        self.set_textgen_things()

    def prompt_generation(self, pre_textgen_mode):
        # Generate a final prompt based on the pre-textgen mode and the user input

        # if pre_textgen_mode == 'default_mode':

        # if pre_textgen_mode == 'notebook_mode':

        if pre_textgen_mode == 'chat_mode':
            if self.instructRadioButton.isChecked():
                # Get the chat preset for instruct mode from a file
                chat_preset = self.get_chat_presets("instruct")

                # Replace the placeholders in the turn template with the user and bot names and messages
                final_prompt = chat_preset["turn_template"]\
                    .replace("<|user|>", chat_preset["user"])\
                    .replace("<|user-message|>", self.chat_modeTextInput.toPlainText())\
                    .replace("<|bot|>", chat_preset["bot"])

                # Remove the bot message placeholder from the final prompt
                match = "<|bot-message|>"
                end_newlines = final_prompt.split(match)[1]
                final_prompt = final_prompt.split(match)[0]
                final_prompt = final_prompt.replace(
                    "<|bot-message|>", "")

                # Add the previous chat history and any newlines to the final prompt
                final_prompt = (
                    f"{self.chat_modeTextHistory.toPlainText()}{end_newlines}{final_prompt}")

            else:
                # Get the chat preset for character mode from a file
                chat_preset = self.get_chat_presets("character")
                # Add the user name, input message and character name to the final prompt
                final_prompt = self.chat_modeTextHistory.toPlainText()+'\n\n'+self.yourNameLine.text()+": "+self.chat_modeTextInput.toPlainText()+'\n' +\
                    chat_preset["name"]+":"
            # Return the final prompt
            return final_prompt

    # Get chat presets from files
    def set_preset_params(self, preset_mode, partial=None):
        # Set the preset parameters based on the preset mode

        if preset_mode == 'instruct':
            # If the preset mode is chat
            self.instructRadioButton.setChecked(True)

            # Get the chat preset for instruct mode from a file
            chat_preset = self.get_chat_presets('instruct')
            # Set the chat mode text history widget to show the context from the preset
            self.chat_modeTextHistory.setPlainText(
                chat_preset["context"].rstrip())

        if preset_mode == 'character':
            # If the preset mode is character
            # Check the character radio button
            self.charactersRadioButton.setChecked(True)
            # Get the chat preset for character mode from a file
            chat_preset = self.get_chat_presets("character")

            # Replace the placeholders in the example dialogue with the character and user names
            final_example_dialogue = chat_preset["example_dialogue"]\
                .replace(r"{{char}}", chat_preset["name"])\
                .replace(r"{{user}}", self.yourNameLine.text())

            # Add the context, greeting and example dialogue to the final prompt
            final_prompt = (chat_preset["context"])\
                + '\n\n'+chat_preset["greeting"]\
                + '\n\n'+final_example_dialogue

            # Set the chat mode text history widget to show the final prompt
            self.chat_modeTextHistory.setPlainText(final_prompt)

    def awesome_prompts(self):
        # Get awesome prompts from a csv file

        filename = "presets/prompts.csv"
        with open(filename, "r",  encoding="utf-8") as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                # If the row matches the current text of the awesome preset combo box
                if row[0] == self.awesomePresetComboBox.currentText():
                    # Set the chat mode text input widget to show the prompt from the row
                    self.chat_modeTextInput.setPlainText(row[1])
                    break


if __name__ == "__main__":
    # Create a Qt application instance
    app = QApplication(sys.argv)

    if platform.system() == 'Windows':
        app.setStyle('Fusion')

    # Create a chat window instance and show it
    window = ChatWindow()
    window.show()

    # Start the Qt event loop
    app.exec()
