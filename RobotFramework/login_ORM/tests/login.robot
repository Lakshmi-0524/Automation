*** Settings ***
Library           SeleniumLibrary
Variables         ../variables/variables.py
Resource          ../resources/keywords.robot

*** Test Cases ***
Valid Login Test
    Launch Browser    ${URL}    ${BROWSER}
    Login To Application    ${USERNAME}    ${PASSWORD}
    Sleep    5s
    Close Application

Invalid Login Test_01
    Launch Browser    ${URL}    ${BROWSER}
    Login To Application    ${USERNAME}    ${PASSWORD_01}
    Sleep    5s
    Close Application

Invalid Login Test_02
    Launch Browser    ${URL}    ${BROWSER}
    Login To Application    ${USERNAME_02}    ${PASSWORD}
    Sleep    5s
    Close Application
