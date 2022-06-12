using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003457: Rolling Thunder
/// </summary>
public class _11003457 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008669$
    // - Someday, I will live up to my father's legacy.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008670$
                // - The people of $map:02000051$ look up to me now. I hope I live up to their expectations.
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
