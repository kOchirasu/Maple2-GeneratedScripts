using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004279: Nazkar Statue
/// </summary>
public class _11004279 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011287$
    // - <font color="#909090">(This is a statue of the guardian deity of Nazkar.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011288$
                // - <font color="#909090">(This is a statue of the guardian deity of Nazkar.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011289$
                // - <font color="#909090">(The $map:02010034$ was the holiest sanctum of the lumarigons, the great dragons of light. Only the worthiest of the worthy could set foot in these halls.)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011290$
                // - <font color="#909090">(In spite of the spreading darkness, there's still a glimmer of the light in this statue's eyes...)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
