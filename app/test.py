from main import hello_world

def test_home():
    response = hello_world()
    assert response == '<p>Hello, World!</p>'

if __name__ == '__main__':
    test_home()