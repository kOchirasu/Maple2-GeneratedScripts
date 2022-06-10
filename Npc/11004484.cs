using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004484: Ambulia
/// </summary>
public class _11004484 : NpcScript {
    internal _11004484(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012258$ 
                // - Keep quiet! Stay down! It's over if the enemy spots us! 
                return true;
            case 10:
                // $script:1227192907012259$ 
                // - Keep quiet! Stay down! It's over if the enemy spots us! 
                switch (selection) {
                    // $script:1227192907012260$
                    // - Something wrong?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012261$ 
                // - Something wrong? Is something <i>wrong</i>?! Look at the chaos out here! I came here to discover new lands, not risk my life! 
                // $script:1227192907012262$ 
                // - That so-called Daemon Army ambushed me, so I ran away... only to find myself in the middle of a Tairen raid! 
                // $script:1227192907012263$ 
                // - At this rate, I'll get tombstoned before I discovery anything worthwhile. If you really want to help, then get rid of those bad guys for me! 
                switch (selection) {
                    // $script:0114161407012705$
                    // - Okay.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0114161407012706$ 
                // - I leave it to you! 
                return true;
            default:
                return true;
        }
    }
}
