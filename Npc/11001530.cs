using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001530: Meminem
/// </summary>
public class _11001530 : NpcScript {
    internal _11001530(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0318211907005934$ 
                // - You feel that? That's music.
                return true;
            case 40:
                // $script:0318211907005938$ 
                // - You feel me? Ask questions if you got any.
                switch (selection) {
                    // $script:0318211907005939$
                    // - How do you play Dance, Dance, Stop?
                    case 0:
                        Id = 41;
                        return false;
                    // $script:0318211907005940$
                    // - I got eliminated. It's not fair!
                    case 1:
                        Id = 47;
                        return false;
                    // $script:0318211907005941$
                    // - What are you doing here?
                    case 2:
                        Id = 48;
                        return false;
                }
                return true;
            case 41:
                // $script:0318211907005942$ 
                // - When the numbers appear on the floor panels, hop on them! If you match the number of dancers to the number, you go on to the next round. Otherwise... you're out!
                switch (selection) {
                    // $script:0318211907005943$
                    // - How do you win? 
                    case 0:
                        Id = 42;
                        return false;
                    // $script:0318211907005944$
                    // - I don't know how to dance.
                    case 1:
                        Id = 46;
                        return false;
                }
                return true;
            case 42:
                // $script:0318211907005945$ 
                // - Last 5 rounds, and you win. But the longer the game goes on, the less time you have to get on a panel. If you're a quick thinker and a fast runner, you can win... even if you're a terrible dancer!
                switch (selection) {
                    // $script:0318211907005946$
                    // - Do you have any tips?
                    case 0:
                        Id = 43;
                        return false;
                    // $script:0318211907005947$
                    // - I'll win next time!
                    case 1:
                        Id = 45;
                        return false;
                }
                return true;
            case 43:
                // $script:0318211907005948$ 
                // - You know I do! Dancing isn't just fun—it's a great way to get experience. Once you're on a tile for 2 or more dancers, you can block others from joining you. This is a great way to lock down a tricky number and get a fabulous bonus.
                // $script:0318211907005949$ 
                // - Just press the action key to block others from joining your panel. You can't leave the tile while you're doing this, so when you're done be sure to press the action key again. But the most important tip I have... is to <i>have fun!</i>
                switch (selection) {
                    // $script:0318211907005950$
                    // - I'll win next time!
                    case 0:
                        Id = 45;
                        return false;
                }
                return true;
            case 45:
                // $script:0318211907005951$ 
                // - That's the spirit! Keep it real, my friend. Keep it real.
                return true;
            case 46:
                // $script:0318211907005952$ 
                // - Don't even sweat it. Just press the yellow light on the floor, and <i>bam!</i> It's dance time! Press the action key to boogie down with some random dance moves.
                switch (selection) {
                    // $script:0318211907005953$
                    // - How do you win? 
                    case 0:
                        Id = 42;
                        return false;
                    // $script:0318211907005954$
                    // - I'll win next time!
                    case 1:
                        Id = 45;
                        return false;
                }
                return true;
            case 47:
                // $script:0318211907005955$ 
                // - Don't let it get to you, my downtrodden dancer. Even if you're eliminated, there's a special dance floor where you can strut yourself. Just go to the yellow stage and press the action key!
                switch (selection) {
                    // $script:0318211907005956$
                    // - What's the secret to winning the game?
                    case 0:
                        Id = 42;
                        return false;
                    // $script:0318211907005957$
                    // - I'll win next time!
                    case 1:
                        Id = 45;
                        return false;
                }
                return true;
            case 48:
                // $script:0318211907005958$ 
                // - Making music isn't the only thing I love, yo. Listening to great jams and partying with my people are high on the list.
                return true;
            default:
                return true;
        }
    }
}