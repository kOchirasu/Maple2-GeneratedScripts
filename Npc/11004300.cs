using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004300: Ghost
/// </summary>
public class _11004300 : NpcScript {
    internal _11004300(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011395$ 
                // - What do you want?
                return true;
            case 30:
                // $script:1002141907011398$ 
                // - I don't gotta answer to you. Now scram, before I get angry.
                switch (selection) {
                    // $script:1002141907011399$
                    // - What brings you here?
                    case 0:
                        Id = 31;
                        return false;
                    // $script:1002141907011400$
                    // - I'm not here to fight, friend.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011401$ 
                // - Blackstar goes where the money is! Here's some free advice: keep your nose outta things where it don't belong.
                switch (selection) {
                    // $script:1002141907011402$
                    // - How'd you become a ghost?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 32:
                // $script:1002141907011403$ 
                // - I ain't your friend, pal! You think you can talk down to me 'cause I'm a ghost? Is that it?
                switch (selection) {
                    // $script:1002141907011404$
                    // - How'd you become a ghost?
                    case 0:
                        Id = 33;
                        return false;
                }
                return true;
            case 33:
                // $script:1002141907011405$ 
                // - To tell the truth... I got no idea. Boss sent me here on a job, and next thing I know... Pow! Ghost.
                switch (selection) {
                    // $script:1002141907011406$
                    // - There, there. It's okay.
                    case 0:
                        Id = 34;
                        return false;
                }
                return true;
            case 34:
                // $script:1002141907011407$ 
                // - I don't want your stinkin' pity! Anyway, this place ain't so bad. It's real cushy, and I got tons of books to read.
                // $script:1002141907011408$ 
                // - Come to think of it, there were some real important-looking papers in one of the books I read the other day. Weird, huh?
                return true;
            default:
                return true;
        }
    }
}
