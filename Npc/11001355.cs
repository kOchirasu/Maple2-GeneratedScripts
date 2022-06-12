using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001355: Lele
/// </summary>
public class _11001355 : NpcScript {
    protected override int First() {
        return 40;
    }

    // Select 0:
    // $script:1216233107005221$
    // - Ah! A human!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:1216233107005225$
                // - We're not supposed to talk to strangers without the captain's approval.
                switch (selection) {
                    // $script:1216233107005226$
                    // - I'm not a stranger. I'm just a friend you haven't met.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1216233107005227$
                // - Beat it! I'm not gonna get in trouble again!
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
