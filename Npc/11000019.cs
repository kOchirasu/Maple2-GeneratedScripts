using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000019: Terry
/// </summary>
public class _11000019 : NpcScript {
    internal _11000019(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000090$ 
                // - Hm hm hmmm, hm! Those marching songs always get stuck in my head. 
                return true;
            case 30:
                // $script:0831180407000093$ 
                // - Hey there. First time in $map:02000062$? 
                switch (selection) {
                    // $script:0831180407000094$
                    // - Yep!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0831180407000095$ 
                // - Well, if you're trying to get to $map:02000001$, I've got some bad news for you.. We just had a big earthquake that split the road there in half. No one can make the journey now. 
                // $script:0831180407000096$ 
                // - As if that weren't bad enough, rough seas are preventing ships from entering or leaving the harbor. We're all stuck here! 
                switch (selection) {
                    // $script:0831180407000097$
                    // - Is there no other way to get to $map:02000001$?
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0831180407000098$
                    // - What about by air?
                    case 1:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:0831180407000099$ 
                // - I've heard there's a wilderness path that connects $map:02000115$ and $map:02000116$, but no one's been taking it. Supposedly it's a bit... dangerous. 
                switch (selection) {
                    // $script:1111011307007374$
                    // - Where's the path?
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:0831180407000100$ 
                // - Uhh... Lith isn't that kind of port, buddy. 
                return true;
            case 34:
                // $script:1111011407007374$ 
                // - It's through a mountain path northwest of $map:02000062$. The path's been closed for ages, though. Too treacherous for most folks. I'd forget about it if I were you. 
                return true;
            default:
                return true;
        }
    }
}
