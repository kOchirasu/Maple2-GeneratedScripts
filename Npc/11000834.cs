using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000834: Cathy Mart Employee
/// </summary>
public class _11000834 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 40;50;60
    }

    // Select 0:
    // $script:0831180407003051$
    // - Welcome to Cathy Mart.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (40, 0):
                // $script:0831180407003055$
                // - When is the next shift going to show up? I really have to go to the bathroom! ...Oh, shoot! Please excuse me, um, how may I help you?
                return -1;
            case (50, 0):
                // $script:0831180407003056$
                // - You can pay for your items at the cashier over there.
                return -1;
            case (60, 0):
                // $script:0831180407003057$
                // - Cathy Mart sells only the highest-quality products. If you find any items that don't seem to meet our standards, please don't hesitate to let me know.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (40, 0) => NpcTalkButton.Close,
            (50, 0) => NpcTalkButton.Close,
            (60, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
