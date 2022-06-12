using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004271: Burgundia
/// </summary>
public class _11004271 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0911203207011241$
    // - <font color="#909090">(This squat desert plant drips with a brilliant red sap.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0911203207011242$
                // - <font color="#909090">(This squat desert plant drips with a brilliant red sap.)</font>
                return 10;
            case (10, 1):
                // $script:0911203207011243$
                // - <font color="#909090">(You're pretty sure you've seen this shade of red in the clothes and makeup worn by the people of Karkar.)</font>
                return 10;
            case (10, 2):
                // $script:0911203207011244$
                // - <font color="#909090">(You've seen plants like this all over Karkar, but they're especially plentiful here.)</font>
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
