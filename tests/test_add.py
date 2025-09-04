import demo_project

def test_add(capsys):
    demo_project.add(2, 3)
    
    #capture stdout/stderr
    captured = capsys.readouterr()
    assert captured.out == "Latheesh Addition worked:  5\n"
    assert captured.err == ""