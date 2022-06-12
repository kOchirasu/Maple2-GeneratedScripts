using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000287: Bag
/// </summary>
public class _11000287 : NpcScript {
    protected override int First() {
    }

    // Select 0:
    // $script:0831180407001127$
    // - Check the altar.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0831180407001128$
                // - This altar is covered in layers of dust, the result of ages of neglect.
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
