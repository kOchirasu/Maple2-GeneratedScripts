using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003166: Joddy
/// </summary>
public class _11003166 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0516084007008466$
    // - I sure hope $npcName:11003163[gender:0]$ comes back soon.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0516084007008469$
                // - I hear $npcName:11003163[gender:0]$ is one of the most dutiful, most devoted, most loving sons in all of Maple World.
                switch (selection) {
                    // $script:0516084007008470$
                    // - He's a devoted... son?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0516084007008471$
                // - Yeah! He's always off visiting his sick ma, who lives really far away. When I finally graduate, I'm gonna be a good son, too!
                switch (selection) {
                    // $script:0516084007008472$
                    // - Why wait until then?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0516084007008473$
                // - If my mom and dad saw me the way I am now, they'd die of shame. Gotta prove myself, first!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
