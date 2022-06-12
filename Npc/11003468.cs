using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003468: Hidden Passage
/// </summary>
public class _11003468 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008673$
    // - <font color="#909090">(You can feel a breeze from beyond the wall. Is there a secret passage?)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008674$
                // - <font color="#909090">(You can feel a breeze from beyond the wall. Is there a secret passage?)</font>
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
