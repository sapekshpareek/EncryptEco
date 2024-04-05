import matplotlib.pyplot as plt

sss_data = {1: 8.000, 2.5: 20.032, 5: 40.032, 10: 80.032, 50: 400.128, 100: 800.224}
aes_data = {1: 16.768, 2.5: 41.536, 5: 83.552, 10: 159.424, 50: 797.792, 100: 1595.584}

sss_time = {1: 0.20008087158203125, 2.5: 0.3000020980834961, 5: 0.40009021759033203, 10: 0.500035285949707, 50: 1.608443260192871, 100: 2.8116226196289062}
aes_time = {1: 0.00000000000000000, 2.5: 0.10013580322265625, 5: 0.10001659393310547, 10: 0.10006427764892578, 50: 0.4001140594482422, 100: 0.7011175155639648}

def storageGraph():
    words_aes = []
    storage_aes = []
    words_sss = []
    storage_sss = []

    for i in aes_data:
        words_aes.append(i)
        storage_aes.append(aes_data.get(i))
        words_sss.append(i)
        storage_sss.append(sss_data.get(i))

    plt.plot(words_aes, storage_aes, label = 'AES')
    plt.plot(words_sss, storage_sss, label = 'SSS')
    plt.xlabel('No. of Words in Thousands')
    plt.ylabel('Storage in Kilo Bytes')
    plt.title('Storage Comparison Between AES and SSS')
    plt.legend()
    plt.show()
    return


def timeGraph():
    words_aes = []
    time_aes = []
    words_sss = []
    time_sss = []

    for i in aes_time:
        words_aes.append(i)
        time_aes.append(aes_time.get(i))
        words_sss.append(i)
        time_sss.append(sss_time.get(i))
    plt.plot(words_aes, time_aes, label = 'AES')
    plt.plot(words_sss, time_sss, label='SSS')
    plt.xlabel('Words in Thousands')
    plt.ylabel('Time in Milliseconds')
    plt.title('Time Comparison Between AES and SSS')
    plt.legend()
    plt.show()

# timeGraph()
# storageGraph()