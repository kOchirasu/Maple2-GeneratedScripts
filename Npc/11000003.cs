using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000003: Growlie
/// </summary>
public class _11000003 : NpcScript {
    internal _11000003(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000015$ 
                // - What? 
                return true;
            case 40:
                // $script:0831180407000018$ 
                // - I don't care why the court was canceled anymore. I've heard every rumor under the sun, and now they're saying it was an earthquake? Ridiculous! All I want now is to kick back. 
                return true;
            case 50:
                // $script:0831180407000019$ 
                // - Bah, everyone acts like they're the busiest person in the world. Everyone here in $map:02000001$ spends their day rushing around like fools. Seriously! 
                return true;
            case 60:
                // $script:1215102407009687$ 
                // - What do you want? 
                switch (selection) {
                    // $script:1215102407009688$
                    // - Have you heard the rumors going around?
                    case 0:
                        Id = 61;
                        return false;
                }
                return true;
            case 61:
                // $script:1215102407009689$ 
                // - For the last time, I'm not adopted! Mom says its normal for babies to come out giant and furry sometimes. If you want a real rumor, you should hear about the giant demons zipping around the sky. 
                switch (selection) {
                    // $script:1215102407009690$
                    // - Giant demons?
                    case 0:
                        Id = 62;
                        return false;
                }
                return true;
            case 62:
                // $script:1215102407009691$ 
                // - You didn't know? It's all anyone's talking about lately. I've heard talk that they've been kidnapping people. 
                switch (selection) {
                    // $script:1215102407009692$
                    // - Do you actually know of any victims?
                    case 0:
                        Id = 63;
                        return false;
                }
                // $script:1215102407009693$ 
                // - Yeah, the appear like a flash of lightning. In the blink of an eye, the person next to you is gone. Just like that! 
                return true;
            case 63:
                // $script:1215102407009694$ 
                // - Err... No. I'm just telling you what I heard! 
                return true;
            default:
                return true;
        }
    }
}
