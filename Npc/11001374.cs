using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001374: Dortov
/// </summary>
public class _11001374 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217144507005352$
    // - Hm...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217144507005355$
                // - I don't care <i>why</i> this place is in shambles. I care that these noisy hooligans are preventing me from doing my job!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
