using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001401: Montino
/// </summary>
public class _11001401 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217193307005401$
    // - Th-this is too high up...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1228164407005741$
                // - I need to climb down sooner or later, but I'm worried that <i>they</i> are still down there.
                switch (selection) {
                    // $script:1228164407005742$
                    // - Who's they?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1228164407005743$
                // - Those robots! They were supposed to help us develop the desert, but they all went crazy!
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
