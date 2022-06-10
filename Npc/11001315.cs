using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001315: Amorro
/// </summary>
public class _11001315 : NpcScript {
    internal _11001315(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005034$ 
                // - It's a beautiful day, isn't it?  
                return true;
            case 40:
                // $script:1227194507005691$ 
                // - People are always asking me if I'm okay living with my gramps. Well, I am! 
                // $script:1227194507005692$ 
                // - I don't care if you think he's a screaming old fart. If you ask me, he's a great man! 
                switch (selection) {
                    // $script:1227194507005693$
                    // - Your grandpa isn't popular, is he?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1227194507005694$ 
                // - They're just jealous of how great he is! Gramps talks loud so people can hear him clearly. Isn't that nice?  
                return true;
            default:
                return true;
        }
    }
}
