import pandas as pd
import qrcode
import PIL
import sys

def generate_data(sheet_path):
  # read in the data from excel, make sure everything is a string
  df = pd.read_excel(sheet_path, dtype=str)
  print(df)
  qr_strings = []
  rows,cols = df.shape
  for i in df.index:
    st = ""
    col_counter = 0
    for col in df.columns:
      # don't put an extra pipe at the end 
      if col_counter == cols-1:
        st += str(df[col][i])
        col_counter = 0
      else:
        st += str(df[col][i]) + '|'
        col_counter += 1
    qr_strings.append(st)

  return qr_strings



def main():
  qr_strings = generate_data(sys.argv[1])
  for qr_st in qr_strings:
    # generate a qr code with the data
    img = qrcode.make(qr_st)
    # save the qr code as an image in the qr directory
    img.save('./qr_codes/' + qr_st.replace('|', '_') + '.png')


if __name__ == '__main__':
  main()
