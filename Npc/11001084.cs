using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001084: Dodo
/// </summary>
public class _11001084 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1216233107005214$
    // - Ah! A human!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1216233107005218$
                // - We're not supposed to talk to strangers without the captain's approval.
                switch (selection) {
                    // $script:1216233107005219$
                    // - I'm not a stranger. I'm just a friend you haven't met.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1216233107005220$
                // - I'm not falling for that. Shoo!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
