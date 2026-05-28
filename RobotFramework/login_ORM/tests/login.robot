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
