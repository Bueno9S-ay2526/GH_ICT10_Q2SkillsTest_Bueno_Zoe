# SkillsTest
from pyscript import display, document


def show_element(e):
    document.getElementById('result').innerHTML = ' ' #deletes content in result
    user_input = document.getElementById('user_input').value.capitalize().strip() #removes sapces and makes it so the first letter of each word is capitalized
    elements = {
        'H':('H','Hydrogen','1','1.008'),
        'He':('He','Helium','2','4.006'),
        'C':('C','Carbon','6','12.011'),
        'N':('N','Nitrogen','7','14.007'),
        'O':('O','Oxygen','8','15.999'),
        'F':('F','Fluorine','9','18.998'),
        'Ne':('Ne','Neon','10','20.1797'),
        'P':('P','Phosphorus','15','30.974'),
        'S':('S','Sulfur','16','32.065'),
        'Cl':('Cl','Chlorine','17','35.45'),
        'Ar':('Ar','Argon','18','39.948'),
        'Se':('Se','Selenium','34','78.96'),
        'Br':('Br','Bromine','35','79.904'),
        'Kr':('Kr','Krypton','36','83.798'),
        'I':('I','Iodine','53','126.90447'),
        'Xe':('Xe','Xenon','54','131.293'),
        'At':('At','Astatine','85','210'),
        'Rn':('Rn','Radon','86','222'),
        'Ts':('Ts','Tennessine','117','294'),   
        'Og':('Og','Oganesson','118','294')
    }

    element_checker = user_input in elements

    element_data = elements.get(user_input, ["", "", "", ""])
    
    display_message = {
        False: f"<b>{user_input}</b> is not a Non-Metal Element.",
        True: f"<b>Element Symbol:</b> {element_data[0]}<br><b>Element Name:</b> {element_data[1]}<br><b>Atomic Number:</b> {element_data[2]}<br><b>Atomic Weight:</b> {element_data[3]}",
    }

    # display(display_message[element_checker], target='result')

    document.getElementById('result').innerHTML = display_message[element_checker]