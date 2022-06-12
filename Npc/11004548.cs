using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004548: Sleeping Rafflesia
/// </summary>
public class _11004548 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0111140307012685$
    // - <font color="#909090">(The rafflesia is highly toxic. This one seems to be slumbering. Try not to wake it up.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0111140307012686$
                // - <font color="#909090">(The rafflesia is highly toxic. This one seems to be slumbering. Try not to wake it up.)</font>
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
