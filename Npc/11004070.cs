using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004070: Moonlight Wolf Statue
/// </summary>
public class _11004070 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0619202207010151$
    // - <font color="#909090">(This statue marks the final resting place of a great warrior from Perion.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0619202207010152$
                // - <font color="#909090">(This statue marks the final resting place of a great warrior from Perion.)</font>
                return 10;
            case (10, 1):
                // $script:0619202207010153$
                // - <i>Even on the darkest night, the great Guardian of Wolfclaw Canyon fought without a hint of fear in his heart.</i>
                return 10;
            case (10, 2):
                // $script:0619202207010154$
                // - <i>Oh, brave warrior of Perion! Death is not the end. Though you are no longer in this world, your heart will be with the tribes always.</i>
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
