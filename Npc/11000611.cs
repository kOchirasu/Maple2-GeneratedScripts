using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000611: 
/// </summary>
public class _11000611 : NpcScript {
    internal _11000611(INpcScriptContext context) : base(context) {
        // TODO: Condition $script:0831180610000869$
        // Id = 20;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610000856$ 
                // - How may I help you?
                return true;
            case 20:
                // $script:0831180610000869$ 
                // - Welcome, $MyPCName$.
                //   It's an honor.
                //   Would you like to enter the Guild Lounge?
                return true;
            case 10:
                // $script:0831180610000857$ 
                // - This <font color="#ffd200">Guild Lounge</font> is for members only.
                //   Did you have a question?
                switch (selection) {
                    // $script:0831180610000858$
                    // - What are guilds?
                    case 0:
                        Id = 11;
                        return false;
                    // $script:0831180610000859$
                    // - What is the guild lounge?
                    case 1:
                        Id = 12;
                        return false;
                }
                return true;
            case 11:
                // $script:0831180610000860$ 
                // - A guild is an alliance of like-minded heroes.
                //   $npc:11000075[gender:1]$ encourages heroes to form guilds, so they can all benefit from each other's talents.
                switch (selection) {
                    // $script:0831180610000861$
                    // - How does one create a guild?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 12:
                // $script:0831180610000862$ 
                // - The Guild Lounge is a special space for members only. 
                //   It <font color="#ffd200">sells a variety of items for guild members</font>.
                // $script:0831180610000863$ 
                // - But even if you're in a guild, you might not be able to buy items. For that, your particular guild has to have the right.
                // $script:0831180610000864$ 
                // - Whether a guild has the right depends on its number of Guild Trophies. Guild Trophies are the combined Hero Trophies of everyone in the guild.
                // $script:0831180610000865$ 
                // - Each item sold at the Guild Lounge <font color="#ffd200">requires a different number of Guild Trophies</font>. So it's beneficial to have as many Trophies as possible at all times.
                switch (selection) {
                    // $script:0831180610000866$
                    // - How does one create a guild?
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0831180610000867$ 
                // - Press <font color="#ffd200">G</font>, and a window will open where you can create a guild.
                //   Each new guild requires approval from the palace, and that costs <font color="#ffd200">5,000 mesos</font>.
                // $script:0831180610000868$ 
                // - If you want to enter the <font color="#ffd200">Guild Lounge</font>, then please create or join a guild.
                return true;
            default:
                return true;
        }
    }
}
