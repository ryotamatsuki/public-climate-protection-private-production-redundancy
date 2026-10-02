"""Generate exact-origin marginal exhibits; no policy-equilibrium solver is used."""
from __future__ import annotations
import csv
from fractions import Fraction as Q
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from exact_marginals import canonical_channels, origin_marginals

ROOT = Path(__file__).resolve().parents[1]
FIG, TAB = ROOT/'figures', ROOT/'tables'


def main():
    FIG.mkdir(exist_ok=True)
    TAB.mkdir(exist_ok=True)
    rows = []
    for i in range(101):
        gamma = Q(440+i, 1000)
        margins = origin_marginals(gamma)
        rows.append({'gamma': str(gamma), **{name: str(value) for name, value in margins.items()}})
    with (TAB/'policy_marginals.csv').open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['gamma', 'MS', 'ML', 'lambda'], lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)
    # Do not leave the obsolete non-Nash equilibrium series in an incremental build.
    (TAB/'policy_regime.csv').unlink(missing_ok=True)
    gs = [float(Q(row['gamma'])) for row in rows]
    fig, ax = plt.subplots(figsize=(6.5, 4.0))
    ax.plot(
        gs,
        [float(Q(row['MS'])) for row in rows],
        label=r'Common-policy marginal $M_S$',
        color='#1f77b4',
        linestyle='-',
        linewidth=1.8,
    )
    ax.plot(
        gs,
        [float(Q(row['ML'])) for row in rows],
        label=r'Unilateral local marginal $M_L$',
        color='#b44b27',
        linestyle='-.',
        linewidth=1.8,
    )
    ax.axhline(0, color='0.35', linewidth=0.8)
    for root, label in (
        (0.474589333418, r'$\gamma_L$'),
        (0.498291221704, r'$\gamma_S$'),
    ):
        ax.axvline(root, color='0.55', linestyle=':', linewidth=0.9)
        ax.text(
            root,
            0.97,
            label,
            transform=ax.get_xaxis_transform(),
            ha='right',
            va='top',
            fontsize=10,
        )
    ax.set(
        xlabel=r'Product substitutability $\gamma$',
        ylabel='Marginal payoff at zero additional protection',
        xlim=(0.44, 0.54),
    )
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    for suffix in ('pdf', 'eps'):
        fig.savefig(
            FIG / f'policy_regime.{suffix}',
            bbox_inches='tight',
            metadata={'Creator': 'Matplotlib'},
        )
    # Journal-facing vector artwork follows Springer figure-file naming.
    fig.savefig(
        FIG / 'Fig1.eps',
        bbox_inches='tight',
        metadata={'Creator': 'Matplotlib'},
    )
    plt.close(fig)
    channels = canonical_channels()
    with (TAB/'channel_decomposition.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['object', 'value', 'exact_value'])
        writer.writerows((name, float(value), str(value)) for name, value in channels.items())
    with (TAB/'channel_decomposition.tex').open('w') as f:
        f.write(r'''\begin{tabular}{lr}\toprule
Component & Marginal effect \\\midrule
Direct protection effect, redundancy fixed & %0.5f \\
Endogenous redundancy response & %0.5f \\
Total coordinated effect & %0.5f \\
Local-government unilateral payoff effect & %0.5f \\\bottomrule
\end{tabular}
''' % tuple(map(float, channels.values())))
    print('generated exact marginal figure and channel table (no equilibrium curve)')


if __name__ == '__main__':
    main()
, color='#1f77b4',
            linestyle='-', linewidth=1.8)
    ax.plot(gs, [float(Q(row['ML'])) for row in rows],
            label=r'Unilateral local marginal $M_L
        ax.text(root, 0.97, label, transform=ax.get_xaxis_transform(),
                ha='right', va='top', fontsize=10)
    ax.set(xlabel=r'Product substitutability $\gamma$',
           ylabel='Marginal payoff at zero additional protection', xlim=(0.44, 0.54))
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    for suffix in ('pdf', 'eps'):
        fig.savefig(FIG/f'policy_regime.{suffix}', bbox_inches='tight', metadata={'Creator': 'Matplotlib'})
    plt.close(fig)
    channels = canonical_channels()
    with (TAB/'channel_decomposition.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['object', 'value', 'exact_value'])
        writer.writerows((name, float(value), str(value)) for name, value in channels.items())
    with (TAB/'channel_decomposition.tex').open('w') as f:
        f.write(r'''\begin{tabular}{lr}\toprule
Component & Marginal effect \\\midrule
Direct protection effect, redundancy fixed & %0.5f \\
Endogenous redundancy response & %0.5f \\
Total coordinated effect & %0.5f \\
Local-government unilateral payoff effect & %0.5f \\\bottomrule
\end{tabular}
''' % tuple(map(float, channels.values())))
    print('generated exact marginal figure and channel table (no equilibrium curve)')


if __name__ == '__main__':
    main()
, color='#b44b27',
            linestyle='-.', linewidth=1.8)
    ax.axhline(0, color='0.35', linewidth=0.8)
    for root, label in ((0.474589333418, r'$\gamma_L
        ax.text(root, 0.97, label, transform=ax.get_xaxis_transform(),
                ha='right', va='top', fontsize=10)
    ax.set(xlabel=r'Product substitutability $\gamma$',
           ylabel='Marginal payoff at zero additional protection', xlim=(0.44, 0.54))
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    for suffix in ('pdf', 'eps'):
        fig.savefig(FIG/f'policy_regime.{suffix}', bbox_inches='tight', metadata={'Creator': 'Matplotlib'})
    plt.close(fig)
    channels = canonical_channels()
    with (TAB/'channel_decomposition.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['object', 'value', 'exact_value'])
        writer.writerows((name, float(value), str(value)) for name, value in channels.items())
    with (TAB/'channel_decomposition.tex').open('w') as f:
        f.write(r'''\begin{tabular}{lr}\toprule
Component & Marginal effect \\\midrule
Direct protection effect, redundancy fixed & %0.5f \\
Endogenous redundancy response & %0.5f \\
Total coordinated effect & %0.5f \\
Local-government unilateral payoff effect & %0.5f \\\bottomrule
\end{tabular}
''' % tuple(map(float, channels.values())))
    print('generated exact marginal figure and channel table (no equilibrium curve)')


if __name__ == '__main__':
    main()
), (0.498291221704, r'$\gamma_S
        ax.text(root, 0.97, label, transform=ax.get_xaxis_transform(),
                ha='right', va='top', fontsize=10)
    ax.set(xlabel=r'Product substitutability $\gamma$',
           ylabel='Marginal payoff at zero additional protection', xlim=(0.44, 0.54))
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    for suffix in ('pdf', 'eps'):
        fig.savefig(FIG/f'policy_regime.{suffix}', bbox_inches='tight', metadata={'Creator': 'Matplotlib'})
    plt.close(fig)
    channels = canonical_channels()
    with (TAB/'channel_decomposition.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['object', 'value', 'exact_value'])
        writer.writerows((name, float(value), str(value)) for name, value in channels.items())
    with (TAB/'channel_decomposition.tex').open('w') as f:
        f.write(r'''\begin{tabular}{lr}\toprule
Component & Marginal effect \\\midrule
Direct protection effect, redundancy fixed & %0.5f \\
Endogenous redundancy response & %0.5f \\
Total coordinated effect & %0.5f \\
Local-government unilateral payoff effect & %0.5f \\\bottomrule
\end{tabular}
''' % tuple(map(float, channels.values())))
    print('generated exact marginal figure and channel table (no equilibrium curve)')


if __name__ == '__main__':
    main()
)):
        ax.axvline(root, color='0.55', linestyle=':', linewidth=0.9)
        ax.text(root, 0.97, label, transform=ax.get_xaxis_transform(),
                ha='right', va='top', fontsize=10)
    ax.set(xlabel=r'Product substitutability $\gamma$',
           ylabel='Marginal payoff at zero additional protection', xlim=(0.44, 0.54))
    ax.legend(frameon=False, loc='lower right')
    fig.tight_layout()
    for suffix in ('pdf', 'eps'):
        fig.savefig(FIG/f'policy_regime.{suffix}', bbox_inches='tight', metadata={'Creator': 'Matplotlib'})
    plt.close(fig)
    channels = canonical_channels()
    with (TAB/'channel_decomposition.csv').open('w', newline='') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['object', 'value', 'exact_value'])
        writer.writerows((name, float(value), str(value)) for name, value in channels.items())
    with (TAB/'channel_decomposition.tex').open('w') as f:
        f.write(r'''\begin{tabular}{lr}\toprule
Component & Marginal effect \\\midrule
Direct protection effect, redundancy fixed & %0.5f \\
Endogenous redundancy response & %0.5f \\
Total coordinated effect & %0.5f \\
Local-government unilateral payoff effect & %0.5f \\\bottomrule
\end{tabular}
''' % tuple(map(float, channels.values())))
    print('generated exact marginal figure and channel table (no equilibrium curve)')


if __name__ == '__main__':
    main()
