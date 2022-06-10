using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003535: Schatten
/// </summary>
public class _11003535 : NpcScript {
    internal _11003535(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1126150707011924$ 
                // - I am the shadow that evil fears.
                return true;
            case 20:
                // $script:1126150707011925$ 
                // - Something on your mind, sweet stuff?
                switch (selection) {
                    // $script:1126150707011926$
                    // - Who are the Shadow Walkers, exactly?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1126150707011927$ 
                // - Tsk, tsk. You should be careful about sticking your nose in Shadow Walker business. I'd hate for something to happen to it.
                switch (selection) {
                    // $script:1126150707011928$
                    // - Well, that's a scary thing to say.
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:1126150707011929$ 
                // - It's for your own good. If you really want to know about us, I'll tell you... when we're a bit <i>closer</i>.
                switch (selection) {
                    // $script:1126150707011930$
                    // - Uh... If you say so...
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1126150707011931$ 
                // - Cheer up, hon. In fact, c'mere and I'll give you a kiss on the cheek!
                switch (selection) {
                    // $script:1126150707011932$
                    // - That's okay! I just remembered I have to... go... away.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1126150707011933$ 
                // - Ha! No need to be shy!
                return true;
            case 40:
                // $script:1126150707011934$ 
                // - Hey there, kitten. Looking to run missions for Dark Wind? I don't think you're ready to handle my business <i>just</i> yet. 
                return true;
            default:
                return true;
        }
    }
}
