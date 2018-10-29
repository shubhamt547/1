import subprocess

class TextInsertions:
        # Insert word as a single word
    def insert_word(self, password):
        p = subprocess.Popen("adb shell input text " + password, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()

        # Insert TEXT with SPACES. To insert text with spaces, use %s instead of spaces
    def insert_text_with_spaces(self, textWithSpaces):

        splitting_text_with_spaces = self.splitting_text_with_spaces(textWithSpaces)
        p = subprocess.Popen("adb shell input text " + splitting_text_with_spaces, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p.wait()
        print(str(output.decode('ascii')))

    def splitting_text_with_spaces(self, textwithspaces):
        text = textwithspaces
        text.split()
        print(text.replace(" ", "%s"))
        return str(text.replace(" ", "%s"))