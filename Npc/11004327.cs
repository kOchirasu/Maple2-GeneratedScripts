using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004327: Rolling Thunder
/// </summary>
public class _11004327 : NpcScript {
    internal _11004327(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011517$ 
                // - Hm...
                return true;
            case 10:
                // $script:1010140307011518$ 
                // - This place is... strange.
                switch (selection) {
                    // $script:1010140307011519$
                    // - I didn't expect to see you here.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011520$ 
                // - Hey! Didn't see you there. I'm here to represent $map:02000051$.
                switch (selection) {
                    // $script:1010140307011521$
                    // - Couldn't you have sent a diplomat?
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:1010140307011522$ 
                // - ...There were things I had to see for myself.
                // $script:1010140307011523$ 
                // - My father appeared to me in a dream. He said that $map:02000051$ would soon face a grave danger...
                // $script:1010140307011524$ 
                // - And then this place showed up. It couldn't be a coincidence, right?
                // $script:1010140307011525$ 
                // - More importantly, $npcName:11004328[gender:1]$ has a bad feeling about all this, and I trust her instincts.
                return true;
            default:
                return true;
        }
    }
}
