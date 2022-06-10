using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004486: Vivipara
/// </summary>
public class _11004486 : NpcScript {
    internal _11004486(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012275$ 
                // - Hey, you're from Maple World, right?
                return true;
            case 10:
                // $script:1227192907012276$ 
                // - Hey, you're from Maple World, right?
                switch (selection) {
                    // $script:1227192907012277$
                    // - Is something wrong?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012278$ 
                // - Everything's wrong! I loathe field work. Everything around here wants to tombstone me. And it's been days since I had a proper bath! This assignment must be a sick joke on the part of my boss.
                // $script:1227192907012279$ 
                // - I miss my lab in Tria. I hope this mission ends soon...
                switch (selection) {
                    // $script:1227192907012280$
                    // - Cheer up!
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012281$ 
                // - I hadn't thought of it that way. Thank you. You cheer up, too!
                return true;
            default:
                return true;
        }
    }
}
