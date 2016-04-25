import pandas as pd
import numpy as np
# Must comment out the following imports to run test
import seaborn
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from pandas import DataFrame, Series


def importer(number):
    df_sum = pd.read_csv('atus_analysis/data/atussum_2014.dat',
                         header=0, nrows=number)
    df_rep = pd.read_csv('atus_analysis/data/atusresp_2014.dat',
                         header=0, nrows=number)
    df_sum = df_sum.rename(columns={'tucaseid': 'TUCASEID'})
    return pd.merge(df_sum, df_rep, on='TUCASEID')


df = importer(None)


def draw_plot_one():
    tempM = df.loc[df['TESEX'] == 1, ['TRCHILDNUM_y', 'TEHRUSLT_y']]
    tempF = df.loc[df['TESEX'] == 2, ['TRCHILDNUM_y', 'TEHRUSLT_y']]

    line1 = tempM['TEHRUSLT_y'].groupby(df['TRCHILDNUM_y']).mean()
    line2 = tempF['TEHRUSLT_y'].groupby(df['TRCHILDNUM_y']).mean()

    plt.plot(line1, color='r')
    plt.plot(line2, color='b')
    plt.yticks([0, 10, 20, 30, 40])
    plt.title('Average Hours Worked by Family Size, Men and Women',
              fontsize=20)
    plt.ylabel('Hours Worked', fontsize=14)
    plt.xlabel('Number of Children', fontsize=14)
    plt.show()


def draw_plot_two():
    temp = list(df['TEAGE'].groupby(df['TEIO1COW']).mean())
    labels = ['Unknown', 'Gov, fed', 'Gov, state', 'Gov, local',
              'Private, for $', 'Private, non$', 'Self-emp, inc',
              'Self-emp, uninc', 'Volunteer']
    y_pos = np.arange(len(labels))
    plt.barh(y_pos, temp, align='center', alpha=0.4)
    plt.yticks(y_pos, labels)
    plt.xlabel('Age', fontsize=14)
    plt.title('Average Age by Occupation Class', fontsize=20)
    plt.show()


def draw_plot_three():
    bins = np.array([0, 15, 20, 25, 30, 35, 40, 45,
                     50, 55, 60, 65, 70, 75, 80, 200])
    groups = df[['t120401', 't120402', 't120403', 't120404',
                 't120499']].groupby(pd.cut(df['TEAGE'], bins))
    output = groups.sum().dropna()

    label_list = ['Performing arts', 'Museums', 'Movies', 'Gambling', 'Other']
    x = np.arange(15)
    y1, y2, y3, y4, y5 = (output['t120401'], output['t120402'],
                          output['t120403'], output['t120404'],
                          output['t120499'])

    fig, ax = plt.subplots()
    stck = ax.stackplot(x, y1, y2, y3, y4, y5)
    ax.set_ylim([0, 9900])
    proxy_rects = [Rectangle((0, 0), 1, 1,
                   fc=pc.get_facecolor()[0]) for pc in stck]
    ax.legend(proxy_rects, label_list)
    plt.title('Total Time Spent Watching Non-Sport Entertainment Arts',
              fontsize=20)
    plt.ylabel('Total Minutes Spent', fontsize=14)
    plt.xlabel('Age Bracket', fontsize=14)
    plt.xticks(np.arange(15), ('<15', '15-19', '20-24', '25-29', '30-34',
                               '35-39', '40-44', '45-49', '50-54', '55-59',
                               '60-64', '65-69', '70-74', '75-79', '>=80'),
               rotation=90)
    plt.draw()
    plt.show()


def draw_plot_four():
    x = df[['t130102', 't130103', 't130104', 't130105',
            't130106', 't130110', 't130113', 't130114',
            't130115', 't130117', 't130120', 't130124',
            't130126', 't130127', 't130129', 't130130',
            't130132', 't130134', 't130199']].sum(axis=1)
    y = df[['t130202', 't130203', 't130204', 't130205',
            't130206', 't130210', 't130213', 't130214',
            't130215', 't130216', 't130218', 't130222',
            't130224', 't130225', 't130226', 't130227',
            't130229', 't130231', 't130299']].sum(axis=1)
    fig, ax = plt.subplots()
    ax.set_ylim([-50, 670])
    ax.set_xlim([-50, 770])
    plt.scatter(x, y, c='red', alpha=0.5)
    plt.title('Total Time Spent Watching or Playing Sports', fontsize=20)
    plt.ylabel('Total Minutes Spent Watching', fontsize=14)
    plt.xlabel('Total Minutes Spent Playing', fontsize=14)
    plt.show()
