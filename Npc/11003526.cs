using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003526: Rain
/// </summary>
public class _11003526 : NpcScript {
    internal _11003526(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009037$ 
                // - What is it?
                return true;
            case 30:
                // $script:0816160115009038$ 
                // - Sh. I'm trying to think of a melody. Can you give me a minute?
                switch (selection) {
                    // $script:0816160115009039$
                    // - Yeah, goodbye.
                    case 0:
                        Id = 36;
                        return false;
                    // $script:0816160115009040$
                    // - (Wait.)
                    case 1:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0816160115009041$ 
                // - ♬ Compelled to capture every pet! You and I, together! ♬
                switch (selection) {
                    // $script:0816160115009042$
                    // - Yeah, goodbye.
                    case 0:
                        Id = 36;
                        return false;
                    // $script:0816160115009043$
                    // - (Wait a little more.)
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 36:
                // $script:0816170815009057$ 
                // - ♬ I wish for unparalleled skill... ♬
                return true;
            case 32:
                // $script:0816160115009044$ 
                // - A fan, are you? Want my autograph? An advanced copy of my album? Well, it's coming out soon, so you'll just have to wait!
                switch (selection) {
                    // $script:0816160115009045$
                    // - I'd like to hear a song.
                    case 0:
                        Id = 33;
                        return false;
                    // $script:0816160115009046$
                    // - I want to know about your pet.
                    case 1:
                        Id = 34;
                        return false;
                }
                return true;
            case 33:
                // $script:0816160115009047$ 
                // - My new song is a secret! You'll have to wait for the single, like everybody else.
                return true;
            case 34:
                // $script:0816160115009048$ 
                // - This one... this one cannot be tamed. It's special.
                switch (selection) {
                    // $script:0816160115009049$
                    // - Where can I get one?
                    case 0:
                        Id = 35;
                        return false;
                }
                return true;
            case 35:
                // $script:0816160115009050$ 
                // - That's my secret!
                return true;
            default:
                return true;
        }
    }
}
