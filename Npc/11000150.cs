using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000150: Justin
/// </summary>
public class _11000150 : NpcScript {
    internal _11000150(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000640$ 
                // - What is it? 
                return true;
            case 30:
                // $script:0831180407000643$ 
                // - People spend their days scrambling around, trying to have it all. That's no way to live. Just enjoy the moment. 
                return true;
            case 40:
                // $script:0321130807008115$ 
                // - Unless this is extremely important, I'm in no mood to chat. 
                switch (selection) {
                    // $script:0321130807008116$
                    // - Did you see a guard get dragged away?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0321130807008117$ 
                // - Now that you mention it, there was an especially pitiful-looking soldier... He was dragged off in the direction of $map:52000119$, to the northeast. 
                return true;
            default:
                return true;
        }
    }
}
