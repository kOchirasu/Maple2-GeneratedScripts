using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003641: Ain
/// </summary>
public class _11003641 : NpcScript {
    internal _11003641(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109121007009124$ 
                // - Hey hey hey! 
                return true;
            case 10:
                // $script:1109121007009125$ 
                // - You here to jam, my friend? Let your inner songbird free! 
                switch (selection) {
                    // $script:1109121007009126$
                    // - ♬There's someone that I seek! And I don't have all week! ♬
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1109121007009127$ 
                // - Ow ow ow, my ears! Did someone hit your songbird with a hammer? 
                switch (selection) {
                    // $script:1109121007009128$
                    // - I... I think I'm gonna cry...
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1109121007009129$ 
                // - Don't be like that, $male:man,female:lady$. Here, I know something what'll cheer you right up. 
                switch (selection) {
                    // $script:1109121007009130$
                    // - Oh?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:1109121007009131$ 
                // - I've got a message for our fabulous friend, $npcName:11003535[gender:1]$. "The unbreakable link between heart and song!" 
                switch (selection) {
                    // $script:1109121007009132$
                    // - Okay...
                    case 0:
                        Id = 14;
                        return false;
                }
                return true;
            case 14:
                // $script:1109121007009133$ 
                // - Cheer up. You probably just had a frog in your throat, friend. 
                return true;
            default:
                return true;
        }
    }
}
