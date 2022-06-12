using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001145: Juko
/// </summary>
public class _11001145 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0915220707003959$
    // - I'm confused... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0915220707003962$
                // - Mmm... Do you like candy?
                switch (selection) {
                    // $script:0915220707003963$
                    // - No. I hate candy, because I am a monster.
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:0915220707003964$
                // - Whaaaat? I'm sure you'd change your mind if you tried my Mom's $item:30000395$. It's awesome!
                switch (selection) {
                    // $script:0915220707003965$
                    // - That's nice.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:0915220707003966$
                // - <font color="#909090">(He whines pitifully)</font>
                //   Just try a piece! I promise you'll love it. My mom also bakes cakes and pies that are crazy good. She's like a <i>witch</i>!
                switch (selection) {
                    // $script:0915220707003967$
                    // - Anyone can bake.
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:0915220707003968$
                // - Not like my mom! When I grow up, I'm going to be a culinary wizard, and make snacks just as good as hers. 
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
