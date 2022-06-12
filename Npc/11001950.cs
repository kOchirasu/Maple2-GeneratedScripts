using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001950: Mareda
/// </summary>
public class _11001950 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1123165007007496$
    // - Can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1208184307007548$
                // - First, I'll learn how to play the harp. Then I'll let my hair down, and wear a flowing white gown, and spend all day plucking on the strings. I'll look so pretty!
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
