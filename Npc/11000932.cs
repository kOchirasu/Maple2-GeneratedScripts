using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000932: Anka's Soul
/// </summary>
public class _11000932 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407003308$
    // - Dear God of Courage, please give me strength... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407003310$
                // - My body my be gone, but my soul still burns.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
