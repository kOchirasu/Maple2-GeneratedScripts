using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004098: Chocolate Waffle Waterfall
/// </summary>
public class _11004098 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0623132607010349$
    // - <font color="#909090">(This chocolate waterfall puts off an overwhelmingly sweet aroma.)</font>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0623132607010350$
                // - <font color="#909090">(This chocolate waterfall puts off an overwhelmingly sweet aroma.)</font>
                return 10;
            case (10, 1):
                // $script:0623132507010346$
                // - <font color="#909090">(The rich chocolate of this waterfall is enough to drive some children sugar-crazy.)</font>
                return 10;
            case (10, 2):
                // $script:0623132507010347$
                // - <font color="#909090">(The chocolate found in $map:02000257$ is favored by dessert chefs everywhere. Some say it's even Empress $npcName:11001969[gender:1]$'s favorite chocolate.)</font>
                return 10;
            case (10, 3):
                // $script:0623132507010348$
                // - <font color="#909090">(In fact, rumor has it the empire's vaults are full of the stuff...)</font>
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Next,
            (10, 2) => NpcTalkButton.Next,
            (10, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
