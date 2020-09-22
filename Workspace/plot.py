import pickle
import matplotlib.pyplot as plt

data = pickle.load(open('waveforms.pickle', 'rb'))
counter = 1
for quake in data:
    if(counter > 1):
        break
    print(str(counter) + '. ', end='')
    counter = counter + 1
    forms = data[quake].waveform
    plt.figure(figsize=(19.2, 10.8))
    print(forms[0])
    plt.plot(forms[0], label='E-W', color = 'red')
    # plt.plot(forms[1], label='N-S', color = 'yellow')
    # plt.plot(forms[2], label='V', color = 'green')
    plt.show()
    # plt.savefig(quake.replace('/', '').replace(',', '').replace(' ', '_').replace(':', '') + '.png')