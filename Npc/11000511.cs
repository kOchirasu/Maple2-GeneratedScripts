using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000511: Elliana Shuabritze
/// </summary>
public class _11000511 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0831180610000580$
    // - What do you want?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // functionID=1 
                // $script:0624180010002188$
                // - Do you have old enchanted equipment you don't need anymore? I'll turn it into a scroll so you can transfer the enchantment to your new gear!
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
