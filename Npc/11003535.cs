using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003535: Schatten
/// </summary>
public class _11003535 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1126150707011924$
    // - I am the shadow that evil fears.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1126150707011925$
                // - Something on your mind, sweet stuff?
                switch (selection) {
                    // $script:1126150707011926$
                    // - Who are the Shadow Walkers, exactly?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1126150707011927$
                // - Tsk, tsk. You should be careful about sticking your nose in Shadow Walker business. I'd hate for something to happen to it.
                switch (selection) {
                    // $script:1126150707011928$
                    // - Well, that's a scary thing to say.
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1126150707011929$
                // - It's for your own good. If you really want to know about us, I'll tell you... when we're a bit <i>closer</i>.
                switch (selection) {
                    // $script:1126150707011930$
                    // - Uh... If you say so...
                    case 0:
                        return 33;
                }
                return -1;
            case (33, 0):
                // $script:1126150707011931$
                // - Cheer up, hon. In fact, c'mere and I'll give you a kiss on the cheek!
                switch (selection) {
                    // $script:1126150707011932$
                    // - That's okay! I just remembered I have to... go... away.
                    case 0:
                        return 34;
                }
                return -1;
            case (34, 0):
                // $script:1126150707011933$
                // - Ha! No need to be shy!
                return -1;
            case (40, 0):
                // $script:1126150707011934$
                // - Hey there, kitten. Looking to run missions for Dark Wind? I don't think you're ready to handle my business <i>just</i> yet. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.SelectableDistractor,
            (33, 0) => NpcTalkButton.SelectableDistractor,
            (34, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
