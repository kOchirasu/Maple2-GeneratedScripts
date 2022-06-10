using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004325: Blake
/// </summary>
public class _11004325 : NpcScript {
    internal _11004325(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011499$ 
                // - Breathtaking!
                return true;
            case 10:
                // $script:1010140307011500$ 
                // - Ahh... It's too beautiful.
                // $script:1010140307011501$ 
                // - Can't you feel it? The stunning aurora in the sky... The alien wildlife... This place is filling me with creative energy!
                // $script:1010140307011502$ 
                // - I feel it brewing inside. I'm ready to write a smash hit song!
                switch (selection) {
                    // $script:1010140307011503$
                    // - Since when do you write your own songs?
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011504$ 
                // - Forget the $npcName:11004325[gender:0]$ you used to know. From this day on, I'm reborn as a guy who totally writes his own songs!
                // $script:1010140307011505$ 
                // - You just wait. The new and improved $npcName:11004325[gender:0]$ is going to take the world by storm!
                return true;
            default:
                return true;
        }
    }
}
