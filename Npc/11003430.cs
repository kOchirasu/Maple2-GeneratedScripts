using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003430: Temple Altar
/// </summary>
public class _11003430 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0706160807008647$
    // - <font color="#909090">(There appears to be an empty space under the altar.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0706160807008648$
                // - <font color="#909090">(There appears to be an empty space under the altar.)</font>
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
