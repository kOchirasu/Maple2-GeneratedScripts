using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003525: Rose
/// </summary>
public class _11003525 : NpcScript {
    internal _11003525(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0816160115009030$ 
                // - Can I help you?
                return true;
            case 30:
                // $script:0816213215009068$ 
                // - We aren't open yet. Can you please come back later?
                switch (selection) {
                    // $script:0816213215009069$
                    // - Of course.
                    case 0:
                        Id = 32;
                        return false;
                    // $script:0816213215009070$
                    // - When are you opening?
                    case 1:
                        Id = 31;
                        return false;
                    // $script:0816213215009071$
                    // - Who runs this place?
                    case 2:
                        Id = 33;
                        return false;
                    // $script:0816213215009072$
                    // - What's that music?
                    case 3:
                        Id = 34;
                        return false;
                }
                return true;
            case 31:
                // $script:0816213215009073$ 
                // - We... don't have a date yet, actually. The boss wants to redecorate and... and hire more people.
                return true;
            case 32:
                // $script:0816213215009074$ 
                // - Watch your step. It's slippery over there.
                return true;
            case 33:
                // $script:0816213215009075$ 
                // - It seems the boss has strange tastes. He asked me to wear this outfit, even though we aren't open yet. It's so uncomfortable...
                return true;
            case 34:
                // $script:0816213215009076$ 
                // - Isn't it cool? It's the $map:61000008$ theme song! The boss doesn't like it, but it's pretty popular these days.
                // $script:0816225215009078$ 
                // - Come to think of it, didn't the boss lose a game of $map:61000008$ the other day...?
                return true;
            default:
                return true;
        }
    }
}
