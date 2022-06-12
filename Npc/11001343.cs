using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001343: Vex
/// </summary>
public class _11001343 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1217012607005292$
    // - I'm busy! Get to the point.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1217012607005295$
                // - Sigh... I can't ever let my guard down at work. Accidents happen all the time, you know.
                switch (selection) {
                    // $script:1217012607005296$
                    // - How old are you?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1217012607005297$
                // - Ahem! Why do you care? I'm old enough, thank you very much.
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
