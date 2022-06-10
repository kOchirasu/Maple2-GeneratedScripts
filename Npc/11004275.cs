using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004275: Numero
/// </summary>
public class _11004275 : NpcScript {
    internal _11004275(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0911203207011264$ 
                // - Ugh, this sucks. When can I get out of here?
                return true;
            case 10:
                // $script:0911203207011265$ 
                // - Ugh, this sucks. When can I get out of here?
                switch (selection) {
                    // $script:0911203207011266$
                    // - What's wrong?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0911203207011267$ 
                // - Who are you, and why is that any of your business?
                switch (selection) {
                    // $script:0911203207011268$
                    // - C'mon. Just tell me what's bothering you.
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:0911203207011269$ 
                // - If you must know, I'm upset because I'm trapped here. There's no way out, and...
                switch (selection) {
                    // $script:0913151207011304$
                    // - Maybe I can help you get free!
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0913151207011305$ 
                // - What? 
                // $script:0911203207011270$ 
                // - Never mind. It's not worth explaining to you. Just move along.
                return true;
            default:
                return true;
        }
    }
}
