using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004289: Beaumarchais
/// </summary>
public class _11004289 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0921211107011340$
    // - For such an old hotel, I suppose this place has its charm.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0921211107011341$
                // - My cousin certainly devoted enough time and money to this place. He passed the hotel to me when he died, but I simply have no interest in running it.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
