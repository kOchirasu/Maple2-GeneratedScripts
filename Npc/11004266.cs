using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004266: Nine
/// </summary>
public class _11004266 : NpcScript {
    internal _11004266(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011207$ 
                // - Breathe in. Breathe out. Stare at the sea. Yes, yes, it's coming back to me now. You've taught me a valuable lesson again today, ocean.
                return true;
            case 10:
                // $script:0911203207011208$ 
                // - Breathe in. Breathe out. Stare at the sea. Yes, yes, it's coming back to me now. You've taught me a valuable lesson again today, ocean.
                // $script:0911203207011209$ 
                // - Yes, ocean, you're right. I must start over with a heart of gratitude. I must devote myself to my training!
                switch (selection) {
                    // $script:0911203207011210$
                    // - Hiiiii! What are you doing?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011211$ 
                // - I am gazing upon the great ocean and filling my heart with peace. I thought the spirit of rock had died within me, but after discussing it with the sea, I realize it had just gone on a little break.
                switch (selection) {
                    // $script:0911203207011212$
                    // - What happened?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0911203207011213$ 
                // - My hands still tremble when I think back upon that day... It was the Maple rock festival, and thousands watched as I made a terrible mistake in the middle of my song. Since then, I've never been able to play that part right.
                switch (selection) {
                    // $script:0911203207011214$
                    // - And the ocean is helping you with that...
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0911203207011215$ 
                // - Yes! Thanks to the ocean's wise advice, I am once again filled with the spirit of rock. Can't you see it shining in my eyes?
                // $script:0911203207011216$ 
                // - Come to my next concert, and you'll see for yourself that I've been transformed by the sea.
                return true;
            default:
                return true;
        }
    }
}
