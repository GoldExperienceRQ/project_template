import app.io.input as inp
import app.io.output as outp
def main():
    input1 = inp.get_console_input()
    outp.write_to_console(input1)
    input2 = inp.read_file("data/file_to_read.txt")
    outp.write_to_file("data/file_to_write.txt", input2)
    input3 = inp.read_file_with_pandas("data/file_to_read.txt")
    outp.write_to_file("data/file_to_write.txt", input3)
    print(input3)
    pass


if __name__ == "__main__":
    main()