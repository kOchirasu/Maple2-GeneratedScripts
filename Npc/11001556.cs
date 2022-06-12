using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001556: Laoz
/// </summary>
public class _11001556 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0617105607006360$
    // - Our minds and bodies follow each other in harmony. Consider, the truly wise speak with wisdom, and also act with wisdom.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0727223007006790$
                // - Finally, you have arrived.
                switch (selection) {
                    // $script:0727223007006791$
                    // - You summoned me?
                    case 0:
                        return 40;
                }
                return -1;
            case (40, 0):
                // $script:0727223007006792$
                // - Indeed. Your training has brought you to an important crossroad. According to our traditions, it is time for you to set out on a journey to test your skills in the outside world.
                return 40;
            case (40, 1):
                // $script:0727223007006793$
                // - However, the presence of this terrible darkness must be dealt with first. We can discuss your training later.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (40, 0) => NpcTalkButton.Next,
            (40, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
